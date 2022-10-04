<template>
  <div>
      <h1>可选课程列表</h1>
      <el-table
            :data="classes"
            stripe
            style="width: 100%">
            <template v-for="(item,index) in headArr">
                console.log(index)
                <el-table-column :key="index" v-if="item.ind===6" :label="item.label" align="center">
                    <template slot-scope="scope">
                        <el-button href="javascript:;" @click="clickchoose(scope.row.course_id)" type="text" size="small">选择</el-button>
                    </template>
                    
                    <!-- <template v-for="(cls,index) in classes">
                        
                    </template> -->
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

  </div>
</template>

<script>
import qs from "qs"
export default {
  name: "ChooseYes",
  components: {},
  props: {},
  data() {
    return {
        classes:[
            // {name:"oo", id:"1", num:"100", info:"面向对象,圣杯之战"},
            // {name:"os", id:"2", num:"100", info:"操作系统,抄就行"},
            // {name:"co", id:"3", num:"100", info:"计组,祭祖"},
            // {name:"intro to ai", id:"4", num:"100", info:"人工智能引论,水课"}
        ],
        headArr:[
            {label:'课程ID', prop:"course_id", ind:1},
            {label:'课程名称', prop:"course_name", ind:2},
            {label:'课程介绍' , prop : 'course_intro', ind:3},
            {label:'剩余人数' , prop : 'course_capacity', ind:4},
            {label:'已选人数', prop : 'course_elected', ind:5},
            {label:'操作', ind:6}
        ],
        student_id:2
    };
  },
  watch: {},
  computed: {},
  methods: {
      find(){
          this.$http({
              method: 'post',
              url: '/api/studentCurriculum',
              data: qs.stringify({
                student_id:this.student_id
              })
          }).then((res) => {
              console.log(res.data.classes)
              this.classes = res.data.classes
          })
      },
      clickchoose(course_id){
          console.log(course_id)
          this.$http({
              method: 'post',
              url: '/api/studentCourseSelection',
              data: qs.stringify({
                course_id:course_id,
                student_id:this.student_id
              })
          }).then((res) => {
            console.log(res.data.success);
            if (res.data.status == 'success'){
                alert("选课成功"); 
                this.$router.push("/chooseclass") // 切换路由
                this.find()
            }
            else{
                alert("人数已满,同学请选择其他课程!")
            }
          })
      }
  },
  created() {
      this.find();
  },
  mounted() {}
};
</script>

<style lang="scss" scoped>

</style>