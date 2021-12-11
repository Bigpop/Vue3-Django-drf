<template>
    <!-- <div v-for="article in info.results" v-bind:key="article.url" id="articles">
        <div class="article-title">
            {{ article.title }}
        </div>
        <div>
            ttttt
        </div>
    </div> -->
    
    <div v-for="item in info" v-bind:key="item.pk" > 
        {{ item.fields.title }} 
        {{item.fields.content}}
    </div>
</template>

<script>

    import axios from 'axios';
    import marked from 'marked';

    export default {
        name: 'App',
        data: function () {
            return {
                info: [],
              
            }
        },
         computed: {
        markdownToHtml(){
            return marked(this.info[0].content);
            }
        },
        mounted() {
            axios
                .get('/api/article/rest-article-list/')
                .then(response => (this.info = response.data))
        }
    }
</script>

<style>
    #articles {
        padding: 10px;
    }

    .article-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
</style>