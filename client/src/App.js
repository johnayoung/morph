import React, { Component, useRef } from 'react';
import AutoLink from './components/AutoLink'
import API from './api';
import WIT from './utils/wit';

class App extends Component {
  constructor(props) {
    super(props);
    this.textInput = null;

    this.setTextInputRef = element => {
      console.log(element);
      this.textInput = element;
    };

    this.focusTextInput = () => {
      // Focus the text input using the raw DOM API
      if (this.textInput) this.textInput.focus();
    };

    this.selectTextInput = () => {
      if (this.textInput) this.textInput.select();
    };
  }
  state = {
    morph: '',
    thinking: false,
    copySuccess: ''
  }

  handleIntent = async e => {
    if(e.key === 'Enter'){
      e.preventDefault();
      try {
        this.setState({thinking: true})
        const {value} = e.target;
        const methods = await API(value);
        const output = methods.data.output
        this.setState({morph: output, thinking: false})
        console.log(this.textInput);
      } catch (err) {
        this.setState({morph: 'I am not smart enough for that...yet', thinking: false})
      }
   }
  }
  
  handleSubmit = async event => {
    event.preventDefault();

    const response = await API(this.state.morph, 'testerinput')
    
    console.log(response);
    console.log(response.data);
  }

  copyToClipboard = (e) => {
    this.textInput.select();
    document.execCommand('copy');
    // This is just personal preference.
    // I prefer to not show the the whole text area selected.
    e.target.focus();
    this.setCopySuccess('Copied!');
    console.log('worked');
  }

  setCopySuccess() {
    this.setState({copySuccess: 'Copied!'})
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
              <div className='flex flex-row justify-center align-center items-center'>
                <span className='inline align-center text-yellow'>https://morph.now.sh/morph/</span>
                <input 
                  className='rounded py-2 px-2 w-full'
                  placeholder='What should we do?' 
                  onKeyPress={(e) => this.handleIntent(e)}
                />
              </div>
              <p className='text-white mt-4 font-hairline text-sm' >Hint: try typing 'uppercase morph'</p>
            </form>
            <p className='text-white mt-16 text-xl'>The answer you seek is: </p>
            {/* <p ref={this.setTextInputRef} className='text-yellow mt-16 text-4xl'>{this.state.morph}</p> */}
            <input 
              type='text' 
              value={this.state.thinking ? 'Working on it...' : this.state.morph} 
              ref={this.setTextInputRef} 
              className={`bg-black text-yellow ${(this.state.morph === 'I am not smart enough for that...yet' ? 'text-m' : 'text-4xl')} text-center w-full`}
            />
            {this.state.morph && 
            <div>
              <button className='bg-yellow px-4 py-2 font-semibold mt-4' onClick={this.copyToClipboard}>Copy</button>
              <p className='mt-2 text-white'>{this.state.copySuccess}</p>
            </div>
            }
          </section>
          <section className='mt-32'>
            <ul className='list-reset text-white flex justify-center items-center'>
              <li className='mb-2 p-4'><a className='text-white hover:text-yellow' href='https://morph.now.sh/'>API</a></li>
              <li className='mb-2 p-4'><a className='text-white hover:text-yellow' href='https://github.com/johnatspreadstreet/morph'>Github</a></li>
            </ul>
          </section>
        </main>
      </div>
    );
  }
}

export default App;
