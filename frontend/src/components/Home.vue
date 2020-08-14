<template>
  <el-container>
    <el-header>
      <el-input placeholder="输入战队名" v-model="team" @keyup.enter.native="search" id="search">
        <el-button slot="append" icon="el-icon-search" type="primary" @click="search"></el-button>
      </el-input>
    </el-header>
    <el-main>
      <el-row type="flex" justify="center">
        <el-col :span="11">
          <el-table :data="record.victory" id="victory">
          <el-table-column label="胜方" prop="winner">
            <template slot-scope="scope">
              <img :src=parseImg(scope.row.winner) alt="" srcset="">
              <span>{{scope.row.winner}}</span>
            </template>
          </el-table-column>
          <el-table-column label="得分" prop="winner_score"></el-table-column>
          <el-table-column label="得分" prop="loser_score"></el-table-column>
          <el-table-column label="败方" prop="loser">
            <template slot-scope="scope">
              <img :src=parseImg(scope.row.loser) alt="" srcset="">
              <span>{{scope.row.loser}}</span>
            </template>
          </el-table-column>
        </el-table>
        </el-col>
        <el-col :span="11">
          <el-table :data="record.defeat" id="defeat">
          <el-table-column label="胜方" prop="winner">
            <template slot-scope="scope">
              <img :src=parseImg(scope.row.winner) alt="" srcset="">
              <span>{{scope.row.winner}}</span>
            </template>
          </el-table-column>
          <el-table-column label="得分" prop="winner_score"></el-table-column>
          <el-table-column label="得分" prop="loser_score"></el-table-column>
          <el-table-column label="败方" prop="loser">
            <template slot-scope="scope">
              <img :src=parseImg(scope.row.loser) alt="" srcset="">
              <span>{{scope.row.loser}}</span>
            </template>
          </el-table-column>
        </el-table>
        </el-col>
      </el-row>
      
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      team: "",
      record: {
        victory: null,
        defeat: null
      }
    }
  },
  methods: {
    search() {
      let that = this;
      this.axios.get("/detail/" + this.team + "/")
        .then(function (response) {
          that.record = response.data;
        })
    },
    parseImg (team) {
      return "/api/media/images/" + team + ".png";
    }
  }
};
</script>

<style lang="stylus" scoped>
.el-input
  width 80%
  margin-left 10%
img
  width 25px
  vertical-align middle
span
  vertical-align middle
</style>
