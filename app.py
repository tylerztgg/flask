from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    username = "aaaaa"
    profile_image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRThRj7Pxl7D1mikqLJEOXfKrnN7m-b7VKtWg&usqp=CAU"

    suggestions = [
        {
            "name": "Tom",
            "img": "https://kb.rspca.org.au/wp-content/uploads/2018/11/golder-retriever-puppy.jpeg",
            "note": "suggested for you",
            "link": "https://www.google.com",
        },
        {
            "name": "Jimmy",
            "img": "https://static.onecms.io/wp-content/uploads/sites/20/2021/04/21/dog-nose.jpg",
            "note": "suggested for you",
            "link": "https://www.google.com",
        },
        {
            "name": "Jack",
            "img": "https://th-thumbnailer.cdn-si-edu.com/VmzPzAffMSDTOUmFSQoh2DmYP0E=/fit-in/1600x0/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/ad/7b/ad7b3860-ad5f-43dc-800e-af57830cd1d3/labrador.jpg",
            "note": "suggested for you",
            "link": "https://www.google.com",
        },
        {
            "name": "Rose",
            "img": "https://media.newyorker.com/photos/5f6cd4dbe1656cfb9de92e71/master/pass/Gupta-DogTourofHouse.jpg",
            "note": "suggested for you",
            "link": "https://www.google.com",
        },
        {
            "name": "Alex",
            "img": "https://www.cityofpaloalto.org/files/assets/public/police-department/animal-services/img_2989.jpg?dimension=pageimage&w=480",
            "note": "suggested for you",
            "link": "https://www.google.com",
        },
    ]

    stories = [
        {
            "name": "Rachel",
            "img": "https://www.utkaltoday.com/wp-content/uploads/2020/09/Rachel-green-Utkal-Today-feat-1.jpg",
        },
        {
            "name": "Monica",
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuD0ipkcBIGny_NQIDLIsfcfz1X9MsE8Z3Vg&usqp=CAU",
        },
        {
            "name": "Ross",
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8522W7Ao6lkusIIpfEglEhxnm-2UWQeKBjg&usqp=CAU",
        },
        {
            "name": "Joey",
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9ZhUERFL-zsXev5-QL-aJB5AAE12JYTNxhg&usqp=CAU",
        },
        {
            "name": "Phoebe",
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTj5IGLqp--p4Xz50lGZgYy4Qa5qrnB_Ds6KQ&usqp=CAU",
        },
    ]

    posts = [
        {
            "user": username,
            "image": "pic1.jpeg",
            "likes": 30,
            "caption": "I really love the sunset in summer. Hope someday I can be back.",
            "more_link": "https://www.google.com",
            "comments": [
                {"user": "Ross", "text": "Yes it was so beautiful!! 😭"},
                {"user": "Michael", "text": "OMG!!! You are such a professional photographer! 🥳"},
            ],
            "time": "1 Day Ago",
        },
        {
            "user": username,
            "image": "pic1.jpeg",
            "likes": 24,
            "caption": "Throwback to my favorite hike from last fall.",
            "more_link": "https://www.google.com",
            "comments": [
                {"user": "Rachel", "text": "This looks amazing!"},
                {"user": "Joey", "text": "How you doin? 😉"},
            ],
            "time": "2 Days Ago",
        },
    ]

    return render_template(
        "home.html",
        username=username,
        profile_image=profile_image,
        suggestions=suggestions,
        stories=stories,
        posts=posts,
    )


if __name__ == "__main__":
    app.run(debug=True)
