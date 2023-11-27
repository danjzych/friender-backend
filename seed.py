from app import db
from models import User, Rating, Image, Message

db.drop_all()
db.create_all()


user1 = User.signup(username='test_user1',
                    password='password',
                    hobbies='skateboarding, cooking',
                    interests='coding at rithm',
                    location=10000,
                    radius=50)

# Hannah
user2 = User.signup(username='test_user2',
                    password='password',
                    hobbies='taking vitamins',
                    interests='testing',
                    location=10002,
                    radius=2)

# Ben
user3 = User.signup(username='test_user3',
                    password='password',
                    hobbies='base jumping',
                    interests='testing',
                    location=10003,
                    radius=2)

# Louis
user4 = User.signup(username='test_user4',
                    password='password',
                    hobbies='mountaineering',
                    interests='Being a chef',
                    location=10004,
                    radius=2)

# Colin
user5 = User.signup(username='test_user5',
                    password='password',
                    hobbies='origami',
                    interests='Tattooing, hardcore punk',
                    location=10005,
                    radius=50)

# Sasha
user6 = User.signup(username='test_user6',
                    password='password',
                    hobbies='calligraphy',
                    interests='testing',
                    location=10006,
                    radius=50)

# Vlad
user7 = User.signup(username='test_user7',
                    password='password',
                    hobbies='juggling',
                    interests='Minimalist Design, Daisy UI',
                    location=10007,
                    radius=50)

user8 = User.signup(username='test_user8',
                    password='password',
                    hobbies='puppetry, soap making',
                    interests='testing',
                    location=10008,
                    radius=50)

user9 = User.signup(username='test_user9',
                    password='password',
                    hobbies='woodworking',
                    interests='testing',
                    location=10012,
                    radius=50)

user10 = User.signup(username='test_user10',
                     password='password',
                     hobbies='living away from people',
                     interests='being alone',
                     location=60002,
                     radius=2)


db.session.commit()
image1 = Image.add_image(
    'test_user1', 'ben-den-engelsen-_mscfMq3kKI-unsplash.jpg')
image2 = Image.add_image(
    'test_user3', 'ben-den-engelsen-_mscfMq3kKI-unsplash.jpg')
image3 = Image.add_image(
    'test_user4', 'louis-hansel-v3OlBE6-fhU-unsplash.jpg')
image4 = Image.add_image(
    'test_user5', 'collins-lesulie-PWK6CeCJtJw-unsplash.jpg')
image5 = Image.add_image(
    'test_user5', 'steven-erixon-SBrxqx8Vvhg-unsplash.jpg')
image6 = Image.add_image(
    'test_user6', 'roth-melinda-gOdqdhU9pWI-unsplash.jpg')
image7 = Image.add_image(
    'test_user7', 'midas-hofstra-a6PMA5JEmWE-unsplash.jpg')
image8 = Image.add_image(
    'test_user2', 'hassan-khan-EGVccebWodM-unsplash.jpg')
image9 = Image.add_image(
    'test_user2', 'jake-nackos-IF9TK5Uy-KI-unsplash.jpg')


rating1 = Rating.add_rating('test_user1', 'test_user2', True)
rating2 = Rating.add_rating('test_user2', 'test_user1', True)
rating3 = Rating.add_rating('test_user3', 'test_user1', True)
rating4 = Rating.add_rating('test_user4', 'test_user1', True)
rating5 = Rating.add_rating('test_user5', 'test_user1', True)
rating6 = Rating.add_rating('test_user6', 'test_user1', True)
rating7 = Rating.add_rating('test_user7', 'test_user1', True)
rating8 = Rating.add_rating('test_user8', 'test_user1', True)
rating9 = Rating.add_rating('test_user9', 'test_user1', True)
rating10 = Rating.add_rating('test_user10', 'test_user1', True)


message1 = Message.add_message(
    'test_user1', 'test_user2', 'Hey! Do you go to the gym on 6th st? I think I\'ve seen you there a couple times')
message2 = Message.add_message(
    'test_user2', 'test_user1', 'Yeah I do! I usually go for the group fitness classes. They are fun but I\'ve been thinking about getting into powerlifting. How long have you been going there?')
message3 = Message.add_message(
    'test_user1', 'test_user2', 'A couple years?')
message4 = Message.add_message(
    'test_user2', 'test_user1', 'Niceee')
message5 = Message.add_message(
    'test_user2', 'test_user1', 'Wanna lift together sometime? Could be fun')
message6 = Message.add_message(
    'test_user1', 'test_user2', 'Yeah! Let\'s do it')
message6 = Message.add_message(
    'test_user2', 'test_user1', 'Also, isn\'t this app awesome? The dude who made this would make a great addition to any engineering team, I bet.')

message8 = Message.add_message(
    'test_user3', 'test_user1', 'Hey! This app is sick. I bet the guy who made it is awesome.')


db.session.commit()
