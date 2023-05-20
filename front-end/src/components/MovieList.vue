<template>
  <div class="movie-list">
    <h3>Movie List</h3>
    <MovieListItem 
    v-for="movie in Todaymovies" :key="movie.id" :movie="movie"
    />
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    Todaymovies() {
      return this.$store.state.today_movies
    }
  }
}
</script>

<style>
.movie-list {
  text-align: start;
}
</style>
