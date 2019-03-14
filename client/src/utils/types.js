export const getType = v =>
  v === undefined ? 'undefined' 
  : v === null ? 'null' 
  : v.constructor.name.toLowerCase();

export const castArray = val => (Array.isArray(val) ? val : [val]);

export const turnString = str => JSON.parse(str.replace(/\'/g,"\""));
