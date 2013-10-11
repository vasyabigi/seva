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
        src: ['<%= app.tmp %>/**/*.js'],
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
            '<%= app.tmp %>/*',
            '<%= app.dist %>/*'
          ]
        }]
      },

      server: 'tmp'
    },

    copy: {
      dist: {
        expand: true,
        cwd: '<%= app.root %>/',
        dest: '<%= app.tmp %>/',
        src: [
          'js/**/*',
          'css/**/*'
        ]
      }
    },

    coffee: {
      dist: {
        files: [{
          expand: true,
          cwd: '<%= app.root %>/coffee',
          src: '{,*/}*.coffee',
          dest: '<%= app.tmp %>/js',
          ext: '.js'
        }]
      }
    },

    watch: {
      scripts: {
        files: '<%= app.root %>/js/**/*',
        tasks: ['jshint']
      },

      coffee: {
        files: '<%= app.root %>/coffee/**/*',
        tasks: ['coffee']
      }
    }

  });

  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-ngmin');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', [
    'jshint',
    'clean:server',
    'copy',
    'coffee',
    'watch'
  ]);

  grunt.registerTask('build', [
    'jshint',
    'clean:dist',
    'copy',
    'coffee',
    'concat',
    'ngmin',
    'uglify'
  ]);

};
