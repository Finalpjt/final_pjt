<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ movie?.movie_id }}</p>
    <p>제목 : {{ movie?.original_language }}</p>
    <p>장르 : {{ movie?.genres }}</p>
    <p>작성시간 : {{ movie?.created_at }}</p>
    <p>수정시간 : {{ movie?.updated_at }}</p>
    <!-- <Comments 
          id=""/> -->
    {{allmovie}}
    {
    "movie_id": 385687,
    "adult": false,
    "original_language": "en",
    "genres": [
        {
            "genre_ids": "Action"
        },
        {
            "genre_ids": "Crime"
        }
    ]
    }
  </div>
</template>

<script>
import axios from 'axios'
// import ArticleList from '@/components/ArticleList.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      allmovie: this.$store.state.movie,
      movie: null,
      
    }
  },
  created() {
    this.getMovieDetail()
    console.allmovie
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
