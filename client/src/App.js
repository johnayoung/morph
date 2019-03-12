import React, { Component } from 'react';
import Select from 'react-select';
import API from './api';
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
        label: `${TOTITLECASE(operation)} - ${desc}`
      }
    });
    this.setState({options: allPaths})

    console.log(response);
    console.log(allPaths);
  }

  handleInputChange = async val => {
    const schema = yup.array();

    const parser = await schema.isValid(val);
    console.log(parser);
    this.setState({morph: val})
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
          <h1 className='text-yellow'>Morph</h1>
          <h2 className='text-white'>A standardized RESTful utility microservice.</h2>
        </header>
        <main className='mt-16 text-center'>
          <section>
            <form onSubmit={this.parseSwagger}>
              <Select 
                autoFocus
                options={this.state.options}
                isMulti
                closeMenuOnSelect={false}
                menuIsOpen={true}
              />
              {/* <Input placeholder='What should we do?' callback={val => this.handleInputChange(val)} />
              <button type="submit" className='bg-black border border-white rounded text-white p-4'>Submit</button> */}
            </form>
          </section>
          <section>
          </section>
        </main>
      </div>
    );
  }
}

export default App;
