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

  handleInputChange = async val => {
    const schema = yup.array();

    const parser = await schema.isValid(val);
    this.setState({morph: val})
  }

  handleIntent = async e => {
    if(e.key === 'Enter'){
      const {value} = e.target;
      const wit = await WIT(value)
      console.log(wit);
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
              {/* <CustomOption 
                options={this.state.options}
                onChange={val => console.log(val)}
              /> */}
              <Select
                autoFocus
                isMulti
                closeMenuOnSelect={false}
                options={this.state.options}
                placeholder='Choose your morphing mechanism...'
                onChange={val => console.log(val)}
              />
              <input 
                className='mt-16'
                placeholder='What should we do?' 
                onKeyPress={(e) => this.handleIntent(e)}
              />
            </form>
            <p className='text-white mt-16'>The answer you seek is: </p>
          </section>
          <section>
          </section>
        </main>
      </div>
    );
  }
}

export default App;
