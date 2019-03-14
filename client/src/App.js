import React, { Component, useRef } from 'react';
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
    dataType: '',
    options: [],
    copySuccess: ''
  }

  handleIntent = async e => {
    if(e.key === 'Enter'){
      e.preventDefault();
      try {
        this.setState({thinking: true})
        const {value} = e.target;
        const wit = await WIT(value)
        const intent = wit.data.entities.api_method;
        const input = wit.data.entities.input;
        const methods = await API(intent[0].value, input[0].value);
        this.setState({morph: methods.data.output, thinking: false})
        console.log(this.textInput);
      } catch (err) {
        this.setState({morph: 'I am not smart enough for that yet', thinking: false})
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
              <input 
                className='mt-16 rounded py-4 px-4 w-full'
                placeholder='What should we do?' 
                onKeyPress={(e) => this.handleIntent(e)}
              />
              <p className='text-white mt-4 font-hairline' >Hint: try typing 'uppercase my string'</p>
            </form>
            <p className='text-white mt-16 text-xl'>The answer you seek is: </p>
            {/* <p ref={this.setTextInputRef} className='text-yellow mt-16 text-4xl'>{this.state.morph}</p> */}
            <input 
              type='text' 
              value={this.state.thinking ? 'Working on it...' : this.state.morph} 
              ref={this.setTextInputRef} 
              className='bg-black text-yellow text-4xl text-center w-full'
            />
            {this.state.morph && 
            <div>
              <button className='bg-yellow px-4 py-2 font-semibold mt-4' onClick={this.copyToClipboard}>Copy</button>
              <p className='mt-2 text-white'>{this.state.copySuccess}</p>
            </div>
            }
          </section>
          <section>
          </section>
        </main>
      </div>
    );
  }
}

export default App;
