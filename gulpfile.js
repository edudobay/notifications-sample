var gulp = require("gulp");
var slim = require("gulp-slim");

gulp.task('slim', function() {
    return gulp.src("html/**/*.slim")
      .pipe(slim())
      .pipe(gulp.dest("public/"));
});

gulp.task('watch', function() {
    gulp.watch('html/**/*.slim', ['slim']);
});

