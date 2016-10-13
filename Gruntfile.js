module.exports = function(grunt){
    grunt.initConfig({
        pkg:grunt.file.readJSON('package.json'),
 
        watch:{
            options:{ livereload:true },
            files:['templates/**'],
            tasks:''
        }
            
    });
 
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.registerTask('server',['watch']);
    };
 