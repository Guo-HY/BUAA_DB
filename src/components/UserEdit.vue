<template>
  <div>
      <h2>编辑用户信息</h2>
      <form action="">
          用户名:<input v-model="user.name" type="text"><br>
          年龄:<input v-model="user.age" type="text"><br>
          生日:<input v-model="user.bir" type="text"><br>
          <input type="button" @click="editUserInfo" value="添加">
      </form>
  </div>
</template>

<script>
    export default {
    name: "UserEdit",
    components: {},
    props: {},
    data() {
        return {
            user:{
                id:"",
                name:"",
            }
        };
    },
    computed: {},
    methods: {
        findOne(){
            this.$http.get("http://rap2api.taobao.org/app/mock/306658/http/user/findOne?id=" + this.user.id).then(res=>{
                console.log(res.data);

                this.user = res.data;
            })
        },
        editUserInfo(){
            this.$http.post("http://rap2api.taobao.org/app/mock/306658/http/user/update", this.user).then(res=>{
                console.log(res);
                if (res.data.success) {
                    this.$router.push("/user")
                }
            })
        }
    },
    created() {
        // 接受路由参数
        console.log("修改组件中获取的id:" + this.$route.query.id)
        this.user.id = this.$route.query.id
        this.findOne();
    },
    mounted() {}
    };
</script>

<style lang="scss" scoped>

</style>