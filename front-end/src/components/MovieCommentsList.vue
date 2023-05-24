<template>
  <div class="">
    <h3>Comments</h3>
    <div v-for="comment in comments"
    :key="comment.id" :comment="comment"
    >
		<p>{{ comment.content }}<button @click="deleteComment(comment.id)">X</button></p>
		</div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieCommentsList',
  components: {
  },

  data() {
    return {
      comments: null,
			comment: null
    }
  },

	created(){
		this.getComments()
	},

  methods: {
    getComments(){
        const id = this.$route.params.id
			// const movie_id = this.$route.params.id
			
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${ id }/allcomments/`,
      })
        .then((res) => {
            this.comments = res.data
            console.log(res.data)
        })
        .catch((err) => {
        console.log(err)
        })
    },
		deleteComment(id){
			const movie_id = this.$route.params.id
			console.log(id)

			axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${ movie_id }`,
				data:{
					id
				}
      })
        .then((res) => {
					this.comments = res.data
					console.log(res.data)
        })
        .catch((err) => {
        console.log(err)
        })
    },
  }
}
</script>

<style>

</style>