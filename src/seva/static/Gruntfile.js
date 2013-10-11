'use strict';

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    jshint: {
      options: {
        jshintrc: '.jshintrc'
      },
      all: ['Gruntfile.js', 'js/app/**/*.js']
    },

    concat: {
      options: {
        separator: ';'
      },
      dist: {
        src: ['js/app/**/*.js'],
        dest: 'js/dist/<%= pkg.name %>.js'
      }
    },

    ngmin: {
      dist: {
        files: [{
          expand: true,
          cwd: 'js/dist/',
          src: '*.js',
          dest: 'js/dist/'
        }]
      }
    },

    uglify: {
      options: {
        banner: '/*! PANDA\'S <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      dist: {
        files: {
          'js/dist/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
        }
      }
    }

  });

  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-ngmin');

  // Default task(s).
  grunt.registerTask('default', ['jshint']);

  grunt.registerTask('build', [
    'jshint',
    'concat',
    'ngmin',
    'uglify'
  ]);

};
