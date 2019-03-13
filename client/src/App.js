import React, { Component } from 'react';
import Select from 'react-select';
import Input from './components/Input';
import API from './api';
import WIT from './utils/wit';
import PARSE from './utils/parseSwagger';
import TOTITLECASE from './utils/toTitleCase';
import {getPath} from './utils/extractPath';
import * as yup from 'yup';

class App extends Component {
  state = {
    morph: '',
    morphType: '',
    locked: false,
    dataType: '',
    options: []
  }

  async componentDidMount() {
    const response = await PARSE();
    const {paths} = response.data;
    const allPaths = Object.keys(paths).map(path => {
      const [,structure,operation] = getPath.exec(path);
      const post = response.data.paths[path].post;
      const get = response.data.paths[path].get;
      console.log('post is ', post);
      const desc = post ? post.summary : get.summary;
      return {
        value: operation, 
        label: `${TOTITLECASE(operation)}`,
        description: desc
      }
    });
    this.setState({options: allPaths})
  }

  handleIntent = async e => {
    if(e.key === 'Enter'){
      e.preventDefault();
      const {value} = e.target;
      const wit = await WIT(value)
      const intent = wit.data.entities.api_method;
      const methods = await API(intent[0].value, value);
      this.setState({morph: methods.data.output})
      console.log(methods.data);
   }
  }
  
  handleSubmit = async event => {
    event.preventDefault();

    const response = await API(this.state.morph, 'testerinput')
    
    console.log(response);
    console.log(response.data);
  }

  render() {
    return (
      <div className="container mx-auto px-2">
        <header className="mt-16 text-center">
          <h1 className='text-yellow text-5xl'>Morph</h1>
          <h2 className='text-white'>A standardized RESTful utility microservice.</h2>
        </header>
        <main className='mx-auto mt-16 text-center max-w-sm'>
          <section>
            <form onSubmit={this.parseSwagger}>
              <input 
                className='mt-16 rounded py-4 px-4 w-full'
                placeholder='What should we do?' 
                onKeyPress={(e) => this.handleIntent(e)}
              />
              <p className='text-white mt-4 font-hairline' >Hint: try typing 'uppercase my string'</p>
            </form>
            <p className='text-white mt-16 text-xl'>The answer you seek is: </p>
            <p className='text-yellow mt-16 text-4xl'>{this.state.morph}</p>
          </section>
          <section>
          </section>
        </main>
      </div>
    );
  }
}

export default App;
