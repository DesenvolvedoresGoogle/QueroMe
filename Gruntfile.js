module.exports = function(grunt) {
  'use strict';

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    meta: {
      options: {
        banner: '/*! <%= pkg.name %> - v<%= pkg.version %> (' + '<%= grunt.template.today("yyyy-mm-dd") %>) */\n'
      },
      path: {
        src: 'assets',
        dest: 'public'
      }
    },


    /* Libraries */
    cssmin: {
      options: {
        stripBanners: true,
        banner: '<%= meta.options.banner %>'
      },
      styles: {
        files: {
          '<%= sass.styles.dest %>': '<%= sass.styles.dest %>'
        }
      }
    },

    concat: {
      scripts: {
        src: ['<%= meta.path.src %>/**/*.js'],
        dest: '<%= meta.path.dest %>/scripts/<%= pkg.name %>.js'
      }
    },

    imagemin: {
      dynamic: {
        files: [{
          expand: true,
          cwd: '<%= meta.path.src %>/',
          src: ['**/*.{png,jpg,gif}'],
          dest: '<%= meta.path.dest %>/'
        }]
      }
    },

    sass: {
      styles: {
        src: ['<%= meta.path.src %>/**/*.scss'],
        dest: '<%= meta.path.dest %>/styles/<%= pkg.name %>.css'
      }
    },

    uglify: {
      options: {
        stripBanners: true,
        banner: '<%= meta.options.banner %>'
      },
      scripts: {
        files: {
          '<%= concat.scripts.dest %>': '<%= concat.scripts.dest %>'
        }
      }
    },

    watch: {
      scripts: {
        files: '<%= concat.scripts.src %>',
        tasks: ['concat']
      },
      styles: {
        files: '<%= sass.styles.src %>',
        tasks: ['sass']
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['sass', 'concat', 'imagemin', 'watch']);
  grunt.registerTask('compile', ['sass', 'concat', 'imagemin', 'cssmin', 'uglify']);
};