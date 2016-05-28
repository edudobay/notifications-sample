var gulp = require("gulp");
var slim = require("gulp-slim");
var sass = require("gulp-sass");
var webpack = require("webpack-stream");

gulp.task('slim', function() {
    return gulp.src("html/**/*.slim")
      .pipe(slim())
      .pipe(gulp.dest("public/"));
});

gulp.task('sass', function() {
    return gulp.src('css/**/*.sass')
      .pipe(sass())
      .pipe(gulp.dest('public/css'));
});

gulp.task('webpack', function() {
    return gulp.src('js/main.js')
      .pipe(webpack(require('./webpack.config.js')))
      .pipe(gulp.dest('public/js'));
});

gulp.task('watch', function() {
    gulp.watch('html/**/*.slim', ['slim']);
    gulp.watch('css/**/*.sass', ['sass']);
    gulp.watch('js/**/*.js', ['webpack']);
});

