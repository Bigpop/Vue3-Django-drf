<template>
  <div v-if="article !== null" class="grid-container">
    <div>
      <h1 id="title">{{ article.title }}</h1>
            <p id="subtitle">
                本文由 {{ article.author.username }} 发布于 {{ formatted_time(article.c_time) }}
                <!-- <span v-if="isSuperuser">
                    <router-link :to="{ name: 'ArticleEdit', params: { id: article.id }}">更新与删除</router-link>
                </span> -->
            </p>
        <div v-html="article.content" class="article-body"></div>
       
    </div>
    <div>
        <h3>目录</h3>
        <div v-html="article.toc" class="toc"></div>
    </div>
  </div>
<!-- <Comments :article="article" />  -->
</template>

<script>
import axios from "axios";

export default {
  name: "ArticleDetail",
  components: {},
  data: function () {
    return {
      article: null,
      md_toc: "md_toc_____",
    };
  },
  mounted() {
    axios
      .get("/api/article/" + this.$route.params.id)
      .then((response) => {    
        this.article = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    formatted_time: function (iso_date_string) {
      const date = new Date(iso_date_string);
      return date.toLocaleDateString();
    },
  },
  computed: {
    isSuperuser() {
      return localStorage.getItem("isSuperuser.myblog") === "true";
    },
  },
};
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: 3fr 1fr;
}
#title {
  text-align: center;
  font-size: x-large;
}
#subtitle {
  text-align: center;
  color: gray;
  font-size: small;
}
</style>

<style>
.article-body p img {
  max-width: 100%;
  border-radius: 50px;
  box-shadow: gray 0 0 20px;
}
.toc ul {
  list-style-type: none;
}
.toc a {
  color: gray;
}
</style>