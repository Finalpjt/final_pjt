<template>
  <div class="">
    <h3>Comments</h3>
    <div v-for="comment in comments"
    :key="comment.id" :comment="comment"
    >
		<p> user_id : {{ comment.user }} / content : {{ comment.content }}<button @click="deleteComment(comment.comment_id)">X</button></p>
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
            console.log('------------------------------')
            console.log(res.data)
            console.log(this.comments.comment_id)
        })
        .catch((err) => {
        console.log(err)
        })
    },
		deleteComment(id){
			const movie_id = this.$route.params.id
			console.log(id)
            console.log(movie_id)
// movies/<int:movie_id>/allcomments/<int:comments_pk>/
			axios({
                method: 'delete',
                url: `${API_URL}/api/v1/movies/${ movie_id }/allcomments/${id}/`,
                        data:{
                            movie_id, id
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