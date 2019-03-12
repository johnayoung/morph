import pathToRegexp from '../../node_modules/path-to-regexp/index';

export const getPath = pathToRegexp('/:data/:operation');

// console.log(regexp.exec('/string/capitalize'));