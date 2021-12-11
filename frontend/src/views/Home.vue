<template>

    <Header/>

    <ArticleList/>

    <Footer/>

</template>

<script>
    import Header from '@/components/Header.vue'
    import Footer from '@/components/Footer.vue'
    import ArticleList from '@/components/article/ArticleList.vue'

    export default {
        name: 'Home',
        components: {Header, Footer, ArticleList}
    }
</script>