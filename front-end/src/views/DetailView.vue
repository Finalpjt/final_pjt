<template>
  <div>
    <h1>Detail</h1>
    <img :src="`https://image.tmdb.org/t/p/w220_and_h330_face/${movie.poster_path}`" alt="" srcset="">
    <p>글 번호 : {{ movie?.movie_id }}</p>
    <p>제목 : {{ movie?.title }}</p>
    <p>장르 : {{ movie?.genres }}</p>
    <p>작성시간 : {{ movie?.created_at }}</p>
    <p>수정시간 : {{ movie?.updated_at }}</p>
    {{movie}}

    <MovieComments/>
    <MovieCommentsList/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieComments from '@/components/MovieComments.vue'
import MovieCommentsList from '@/components/MovieCommentsList.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    MovieComments, MovieCommentsList
  },
  data() {
    return {
      // allmovie: this.$store.state.movie,
      movie: null,
    }
  },
  created() {
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
    }
  }
}
</script>
