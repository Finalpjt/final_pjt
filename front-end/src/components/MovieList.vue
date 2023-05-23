<template>
  <div class="">
    <h3>Movie List</h3>
		<div>
			<button @click="first(page)"> first </button>
			<button v-if="page-1!=0" @click="result(page-1)"> {{ page-1 }} </button>
			<button @click="result(page)"> {{ page }}</button>
			<button @click="result(page+1)"> {{ page+1 }}</button>
			<button v-if="page-1==0" @click="result(page+2)"> {{ page+2 }} </button>

		</div>
		<br><br>
		<div class="row row-cols-1 row-cols-md-5 g-4">
    <div v-for="movie in AllMovies" :key="movie.id" :movie="movie">
			<!-- {{movie.title}} -->
			<router-link :to="{
      name: 'DetailView',
      params: {id: movie.movie_id }}">
			<div class="col">
        <div class="card h-100">
            <img :src="`https://image.tmdb.org/t/p/w220_and_h330_face/${movie.poster_path}`" class="card-img-top" alt="" srcset="">
            <div class="card-body h-100">
                <h5 class="card-title">
                    {{ movie.title }}
                </h5>
                <!-- <p class="card-text">
                    {{ movie.overview }}
                </p> -->
            </div>
        </div>
        </div>
      </router-link>
		</div>
		</div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieList',

	data() {
		return {
			page:1,
			AllMovies:null
		}
	},

  computed: {
    // Todaymovies() {
    //   return this.$store.state.today_movies
    // }
  },
	
	methods: {
		first() {
			this.page = 1
			this.pagination
		},
		result(page) {
			this.page=page
			this.pagination()
		},
		pagination() {
			const page = this.page
			axios({
				method: 'get',
				url: `${API_URL}/api/v1/movies/page=${ page }`,
			})
			.then((res) => {
				console.log(res.data)
				this.AllMovies = res.data
      })
      .catch((err) => {
      console.log(err)
      })
		}
	}
}
</script>

<style>

</style>
