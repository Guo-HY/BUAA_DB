<template>
  <div>
      <h1>学生列表</h1>
      <!-- 没写删除修改的方法 -->
      <el-table
            :data="students"
            stripe
            style="width: 100%">
            <template v-for="(item,index) in headArr">
                console.log(index)
                <el-table-column :key="index" v-if="item.ind===4" :label="item.label" align="center">
                    <!-- <template v-for="(user,index) in students"> -->
                    <el-button href="" type="text" size="small">删除</el-button>
                    <el-button type="text" size="small">
                        <a href="">修改</a>
                    </el-button>
                    <!-- </template> -->
                </el-table-column>
                <el-table-column :key="index" v-else :prop="item.prop" :label="item.label" align="center">
                    <template scope="scope">
                        <span>
                            {{scope.row[item.prop]}}
                        </span>
                    </template>
                </el-table-column>
            </template>    
        </el-table>

      <!-- <table border="1">
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
      </table> -->
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
                ],
                headArr:[
                    {label:'ID', prop:"id", ind:1},
                    {label:'姓名' , prop : 'name', ind:2},
                    {label:'年龄' , prop : 'age', ind:3},
                    {label:'操作', ind:4}
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