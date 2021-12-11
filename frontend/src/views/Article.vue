<template>

    <Header/>
    
    <ArticleDetail/>
   
</template>

<script>
    import Header from '@/components/Header.vue'
    import ArticleDetail from '@/components/article/ArticleDetail.vue'
    export default {
        name: 'Article',
        components: {Header, ArticleDetail},
    }
</script>

