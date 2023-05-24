<template>
	<div>
    <h1>MovieRecommend</h1>
    <div class="row row-cols-1 row-cols-md-3 g-4">
        <!-- {{like_movies}} -->
    <div
    v-for="recommend_movie in recommend_movies" :key="recommend_movie.id" :movie="movie"
    >
    <div class="card" @click="reload()">
      
        <router-link :to="{
          name: 'DetailView',
          params: {id: recommend_movie.movie_id }}">
          <div class="card h-100">
          <img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${recommend_movie.poster_path}`" alt="" srcset="">
          
          </div>
        </router-link>
      
    </div>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieRecommendProfile',
  props: {
    like_movies: Array,
  },
  data() {
    return {
      recommend_movies: [],
      like_movie: null,
    }
  },
  computed: {
    like_movies_computed() {
       return this.like_movies
    }
  },
  created(){
    this.recommendMovies()
  },
  methods: {
    recommendMovies(){
      console.log(this.like_movies)
      console.log('일단 like_movie확인')
      const movie_title = this.like_movies
      console.log('---------------------')
      console.log(movie_title)

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/recommends/profile/`,
        data: {
          movie: movie_title
        }
      })
      .then((res) => {
        console.log(res)
        console.log(res.data)
        this.recommend_movies = res.data
        console.log(this.recommend_movies)

      })
      .catch((err) => {
        console.log(err)

      })

    },
    reload() {
      location.reload(true)
    }
  }
}
</script>