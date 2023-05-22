<template>
  <div class="article-list">
    {{ movie?.movie_id }}
    <h3>Comments</h3>
    <input @click.keyup="">
    <button @click=""></button>
    <p
    v-for="comment in comments" :key="comment.id" :comment="comment"
    ></p>
  </div>
</template>

<script>
// import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'Comment',
  components: {
    // ArticleListItem,
  },
  computed: {
    comments() {
      return this.$store.state.comments
    }
  }
}
</script>

<style>

</style>


<template>
  <div>
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
