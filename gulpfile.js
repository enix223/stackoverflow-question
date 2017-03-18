var gulp = require('gulp'),
    shell = require('gulp-shell');


gulp.task('default', shell.task([
    'git pull origin master',
    'source $bae/bin/activate; python manage.py dumpdata > fixtures/data.json',
    'source $bae/bin/activate; python manage.py loaddata fixtures/data.json'
]));

