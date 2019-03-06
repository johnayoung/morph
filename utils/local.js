'use strict';

// Starts python server on local
const args = [ '../api/index.py' ];
const opts = { stdio: 'inherit', cwd: 'client', shell: true };
require('child_process').spawn('python', args, opts);