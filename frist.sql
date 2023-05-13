var express = require('express');
var router = express.Router();
var mysql = require('mysql');
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'blog',
    socketPath: '/var/run/mysqld/mysqld.sock'
});

connection.connect();
module.exports = router