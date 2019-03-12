import React from 'react';
import Select, { components } from 'react-select';

const Option = (props) => {
  return (
    <components.Option {...props}/>
  );
};

export default (props) => (
  <Select
    autoFocus
    isMulti
    closeMenuOnSelect={false}
    components={{ Option }}
    styles={{ option: (base) => ({ ...base, border: `1px dotted`, height: '100%' }) }}
    options={props.options}
    placeholder='Choose your morphing mechanism...'
    onChange={props.onChange}
  />
)