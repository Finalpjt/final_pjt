<template>
  <div>
    <h1>Detail</h1>
    <img style="height: 600px" :src="`https://image.tmdb.org/t/p/w220_and_h330_face/${ movie.poster_path }`" alt="" srcset="">
    <p>글 번호 : {{ movie?.movie_id }}</p>
    <p>제목 : {{ movie?.original_title }}</p>
    <p>장르 : {{ movie?.genres }}</p>
    <p>작성시간 : {{ movie?.created_at }}</p>
    <p>수정시간 : {{ movie?.updated_at }}</p>
    {{movie}}
    <button @click="getlikes()">button</button>
    <MovieRecommend v-bind:movie="movie"/>
    <MovieComments/>
    <!-- <MovieCommentsList/> -->
  </div>
</template>

<script>
import axios from 'axios'
import MovieRecommend from '@/components/MovieRecommend.vue'
import MovieComments from '@/components/MovieComments.vue'
// import MovieCommentsList from '@/components/MovieCommentsList.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    MovieRecommend, MovieComments
  },

  data() {
    return {
      // allmovie: this.$store.state.movie,
      movie: null,
      user: this.$store.state.user,
      username: this.$store.state.username,
      email: this.$store.state.email,
    }
  },
  created() {
    this.getUser(),
    this.getMovieDetail()
    // console.allmovie
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${ this.$route.params.id }`,
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUser() {
      this.$store.dispatch('getUser')
      
    },
    getlikes() {
      console.log(this.$route.params.id)
      // const movie_id = this.$route.params.id
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${ this.$route.params.id }/likes/`,
        // data:{
        //   movie_id
        // },
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
