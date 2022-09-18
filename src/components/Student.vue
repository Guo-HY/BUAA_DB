<template>
  <div>
      <h1>学生列表</h1>
      <img src="../assets/logo.png" alt="">

      <table border="1">
        <tr>
            <td>id</td>
            <td>name</td>
            <td>age</td>
            <td>operation</td>
        </tr>
        <tr v-for="student in students" :key="student.index">
            <td>{{student.id}}</td>
            <td>{{student.name}}</td>
            <td>{{student.age}}</td>
            <td><a href="">删除</a><a href="">修改</a></td>
        </tr>
      </table>
      <Footer></Footer>
  </div>
</template>

<script>
    import Footer from './Footer'
    export default {
        name: "Student",
        data(){
            return{
                students:[
                    {id:"1",name:"zlb",age:18},
                    {id:"2",name:"zbl",age:81}
                ]
            }
        },
        components:{
            Footer
        }
    };
</script>

<style lang="scss" scoped>

</style>