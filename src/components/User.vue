<template>
  <div>
    <h1>用户列表</h1>
    
    <table border="1">
        <tr>
            <td>id</td>
            <td>name</td>
            <td>age</td>
            <td>birth</td>
            <td>operation</td>
        </tr>
        <tr v-for="usr in users" :key="usr.index">
            <td>{{usr.id}}</td>
            <td>{{usr.name}}</td>
            <td>{{usr.age}}</td>
            <td>{{usr.bir}}</td>
            <!-- href="javascript:;" 代表的是发生动作时执行一段javascript代码，但是这个代码是空的，所以什么也不执行 -->
            <!-- 如果用href="",也是会什么都不做但是会刷新页面 -->
            <td><a href="javascript:;" @click="delRow(usr.id)">删除</a><a :href="'#/user/edit?id=' + usr.id">修改</a></td>
        </tr>
    </table>

    <a href="#/user/add">添加</a>
    <!-- 展示路由具体页面 -->
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>

<script>
    import Footer from './Footer'
    export default {
        name: "User",
        data(){
            return{
                users:[
                    // {id:"1",name:"zlb",age:18},
                    // {id:"2",name:"zbl",age:81}
                ]
            }
        },
        methods:{
            findAll(){  //查询所有
                this.$http.get("http://rap2api.taobao.org/app/mock/306658/http/user/findAll?page=1&rows=4").then((res) => {
                    this.users = res.data.results;
                })
            },
            delRow(id){
                console.log(id);
                this.$http.get("http://rap2api.taobao.org/app/mock/306658/http/user/delete?id=" + id).then((res) => {
                    console.log(res)
                    if (res.data.success) {
                        alert(res.data.msg + ",点击确定刷新当前数据")
                        // findAll无变化是因为这里的url是用rap构建的假接口,里面的数据固定所以不会刷新,到时候这儿换成数据库的接口就可以书信了
                        this.findAll();
                    }
                })
            }
        },
        components:{
            Footer
        },
        created(){
            //axios请求
            //url基于后端
            this.findAll();    
        },
        watch:{ //用来监听...
            $route:{    //监听路由变换
                handler: function(val, oldVal){
                    console.log(val)    // 打印变换后的路由
                    if (val.path == "/user") {
                        this.findAll()
                    }
                },
                // 深度监听
                deep:true
            }
        }
    };
</script>

<style lang="scss" scoped>

</style>