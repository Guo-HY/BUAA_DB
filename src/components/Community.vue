<template>
    
  <div>
    <!-- 走马灯 -->
      <el-carousel :interval="4000" type="card" height="bannerH +'px'">
          <el-carousel-item v-for="item in recommendList" :key="item">
            <div class="pic_item">
              <img class="img" :src="item.pic" :alt="item.name">
              <h3>{{item.name}}</h3>
            </div>
          </el-carousel-item>
      </el-carousel>

      <!-- 圈子列表 -->
      <el-table
      :data="allgroups"
      border
      stripe
      style="width: 100%">
      <el-table-column
        prop="name"
        label="圈名"
        width="180">
        <template slot-scope="scope">
          <el-button href="javascript:;" @click="intoGroup(scope.row.groupId)" type="text" size="small">{{scope.row.name}}</el-button>
        </template>
      </el-table-column>
      <el-table-column
        prop="desc"
        label="简介"
        >
      </el-table-column>
      <el-table-column
        prop="tags"
        label="标签">
        <template slot-scope="scope">
          <template v-for="item in scope.row.tags">
            <el-tag>{{item}}</el-tag> 
            &#12288;
          </template>
          
        </template>
      </el-table-column>
      </el-table>

    <el-button type="text" @click="dialog = true">添加圈子</el-button>
    <el-drawer
    title="同学,请填写以下信息来创建自己感兴趣的圈子"
    :before-close="userAddGroup"
    :visible.sync="dialog"
    direction="ltr"
    custom-class="demo-drawer"
    ref="drawer"
    >
    <div class="demo-drawer__content">
      <el-form :model="form">
        <el-form-item label="圈子名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="圈子简介" :label-width="formLabelWidth">
          <el-input v-model="form.desc" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="圈子标签" :label-width="formLabelWidth">
          <el-input v-model="form.tags" autocomplete="off"></el-input>
        </el-form-item>
        <!-- <el-form-item label="活动区域" :label-width="formLabelWidth">
          <el-select v-model="form.region" placeholder="请选择活动区域">
            <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option>
          </el-select>
        </el-form-item> -->
      </el-form>
      <div class="demo-drawer__footer">
        <el-button @click="cancelForm">取 消</el-button>
        <el-button type="primary" @click="$refs.drawer.closeDrawer()" :loading="loading">{{ loading ? '提交中 ...' : '确 定' }}</el-button>
    </div>
  </div>
</el-drawer>

  </div>
</template>

<script>
import qs from "qs"

export default {
  name: "Community",
  components: {},
  props: {
  },
  data() {
    return {
        bannerH:200,
        user_id:this.$store.state.user_id,
        dialog: false,
        loading: false,
        allgroups:[
            {groupId:0, name:'原神', desc:'手游顶流', tags:['game', 'all-platform']},
            {groupId:1, name:'LOL', desc:'网游巅峰', tags:['MOBA']},
            {groupId:3, name:'明星',desc:'追星聚集地', tags:['stars']}
        ],
        recommendList:[
            {groupId:0,pic:'https://tieba-ares.cdn.bcebos.com/mis/2022-11/1668326414661/6f33291a4d2a.jpg', name:'王者荣耀世界', },
            {groupId:1,pic:'https://tieba-ares.cdn.bcebos.com/mis/2022-11/1668325946317/cb4634e49cd7.png', name:'为爱冲锋'},
            {groupId:2,pic:'https://tieba-ares.cdn.bcebos.com/mis/2022-11/1668326060439/20029cea925c.jpg', name:'朱一龙获奖'}
        ],
        form: {
          name: '',
          tags: [],
          desc: ''
        },
        formLabelWidth: '80px',
        timer: null,
    };
  },
  watch: {},
  computed: {},
  methods: {
      getAll(){
        this.$http({
              method: 'post',
              url: '/getCommunityInfo',
              data: qs.stringify({
                user_id:this.user_id
              })
          }).then((res) => {
              console.log(res.data)
            //   this.classes = res.data.classes
          })
      },
      getHotGroupPic(){
        this.$http({
              method: 'post',
              url: '/getHotGroupPic',
              data: qs.stringify({
                user_id:this.user_id
              })
          }).then((res) => {
              console.log(res.data)
              this.recommendList = res.data.groups
          })
      },
      setBannerH(){
        this.bannerH = document.body.clientWidth / 4 + 100
      },
      getHotGroupIntro(){
        this.$http({
              method: 'post',
              url: '/getHotGroupIntro',
              data: qs.stringify({
                user_id:this.user_id
              })
          }).then((res) => {
              console.log(res.data)
              this.allgroups = res.data.groups
          })
      },
      userAddGroup(done){
        if (this.loading) {
          return;
        }
        this.$confirm('确定要提交表单吗？')
        .then(_ => {
          this.loading = true;
          this.timer = setTimeout(() => {
            done();
            // this.$http({
            //     method: 'post',
            //     url: '/userAddGroup',
            //     data: qs.stringify({
            //       userId:this.user_id,
            //       group_name:this.form.group_name,
            //       group_desc:this.form.group_description
            //     })
            // }).then((res) => {
            //     alert("添加成功!")
            // })

            
            // 动画关闭需要一定的时间
            setTimeout(() => {
                this.loading = false;
              }, 400);
            }, 2000);
            console.log(this.form)
        })
        .catch(_ => {});
      },
      cancelForm() {
        this.loading = false;
        this.dialog = false;
        clearTimeout(this.timer);
      },
      intoGroup(id){
        console.log(id)
        this.$store.commit("setGpId", id)
        this.$router.push("/group")
      }
  },
  created() {this.getAll()},
  mounted() {
    this.setBannerH()
    window.addEventListener('resize', () => {
      this.setBannerH()
    }, false)
  }
};
</script>

<style lang="scss" scoped>
    .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 500px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  .pic_item {
  position: relative;
  height: 100%;
  }

  .pic_item h3 {
  position: absolute;
  left: 1rem;
  bottom: 2rem;
  color: white;
}
</style>