<template>
	<div>
    <h1>MovieRecommend</h1>

	<input ref="cursor" type="text" v-model="recommend_movie" @keyup.enter="recommendMovies()" value="recommend">
    <button @click="recommendMovies()">recommend</button>

  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieRecommend',
  data() {
    return {
      recommendmovie: null,
    }
  },
  // created(){
  //   this.getAllActors()
  // },
  // mounted() {
  //   this.startCursor()
  // },
  methods: {
    recommendMovies(){
      const movie = this.recommendmovie

      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/movies/recommends/`,
        data: {
          movie
        }
      })
      .then((res) => {
        console.log(res)
        console.log(res.data)

      })
      .catch((err) => {
        console.log(err)

      })

    },
  }
}
</script>