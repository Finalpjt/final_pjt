<template>
  <div>
    <h1>Detail</h1>
    <img style="height: 600px" :src="`https://image.tmdb.org/t/p/w220_and_h330_face/${ movie.poster_path }`" alt="" srcset="">
    <p>글 번호 : {{ movie?.movie_id }}</p>
    <p>제목 : {{ movie?.eng_title }}</p>
    <p>한국어 제목 : {{ movie?.title }}</p>
    <p>장르 :
    <ul v-for="genre in movie.genres" :key="genre">
        {{ genre.genre_ids }}
    </ul>
    </p>
    <p>청소년 관람 불가 : {{ movie?.adult }}</p>
    <p>영화 평점 : {{ movie?.vote_average }} </p>
    <p>영화 총점 : {{ movie?.popularity }} </p>
    <p>개봉일 : {{ movie?.release_date }} </p>
    <p>영화 줄거리 : {{ movie?.overview }}</p>
    <br><br>
    <p>관련 공식 영상</p>
    <ul v-for="(video, idx) in movie.videos" :key="video">
        <a :href="video.video">video {{ idx + 1 }}</a>
    </ul>
    <p>좋아요를 누른 사람 : {{ movie.like_users }} </p>
    <button @click="getlikes()">ㅈㅇㅇ</button>
    <li v-if="movie.like_users.indexOf(user.pk) !== -1">
        <p>내가 좋아요를 누른 영화다 임마!</p>
    </li>
    <li v-else>
        <p>내가 좋아요를 누르지 않은 영화다 자시가!</p>
    </li>
    <!-- </button> -->
    <!-- <br><br> -->
    <br>
    <MovieRecommend v-bind:movie="movie"/>
    <br>
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
    console.log(this.user)
    console.log('유저 네임 확인용')
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
        console.log(res.data)
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
      const movie_id = this.$route.params.id
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${ this.$route.params.id }/likes/`,
        data:{
          movie_id
        },
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
