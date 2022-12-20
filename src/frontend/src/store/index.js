import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id:2,
    groupId:1,
    postId:4,
    commentid:1,
    other_user_id:1,
  },
  mutations: {
    setUser(state,id){
      state.user_id=id
    },
    setGpId(state,id){
      state.groupId=id
    },
    setCmid(state,id){
      state.commentid=id
    },
    setPostid(state,id){
      state.postId=id
    },
    setOtherid(state,id){
      state.other_user_id=id
    }
  },
  actions: {
  },
  modules: {
  }
})
