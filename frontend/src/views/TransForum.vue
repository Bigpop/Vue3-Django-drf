<template>

    <Header/>
 
    <TransForumCore/>
        
    <Footer/>

</template>

<script>
    import Header from '@/components/Header.vue'
    import Footer from '@/components/Footer.vue'
    import TransForumCore from '@/components/transforum/TransForumCore.vue'

    export default {
        name: 'TransForum',
        components: {Header, Footer, TransForumCore}
    }
</script>

