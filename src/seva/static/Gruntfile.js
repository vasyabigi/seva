'use strict';

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    app: {
      'root': 'app',
      'tmp': 'tmp',
      'dist': 'dist'
    },

    jshint: {
      options: {
        jshintrc: '.jshintrc'
      },
      all: ['Gruntfile.js', '<%= app.root %>/**/*.js']
    },

    concat: {
      options: {
        separator: ';'
      },

      dist: {
        src: ['<%= app.root %>/**/*.js'],
        dest: '<%= app.dist %>/js/<%= pkg.name %>.js'
      }
    },

    ngmin: {
      dist: {
        files: [{
          expand: true,
          cwd: '<%= app.dist %>/js',
          src: '*.js',
          dest: '<%= app.dist %>/js'
        }]
      }
    },

    uglify: {
      options: {
        banner: '/*! PANDA\'S <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      dist: {
        files: {
          '<%= app.dist %>/js/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
        }
      }
    },

    clean: {
      dist: {
        files: [{
          dot: true,
          src: [
            '<%= app.tmp %>',
            '<%= app.dist %>/*'
          ]
        }]
      },

      server: 'tmp'
    }

  });

  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-ngmin');
  grunt.loadNpmTasks('grunt-contrib-clean');

  // Default task(s).
  grunt.registerTask('default', [
    'jshint'
  ]);

  grunt.registerTask('build', [
    'jshint',
    'concat',
    'ngmin',
    'uglify'
  ]);

};
