from app import app, db, Container, Item

with app.app_context():
    container1 = Container(name='Plastic Tote')
    container2 = Container(name='Box of Books')
    container3 = Container(name='Drawer')

    item1 = Item(name='Bathroom Cleaner', container=container1)
    item2 = Item(name='Scrubbing Sponge', container=container1)
    item3 = Item(name='The C Programming Language', container=container2)
    item4 = Item(name='Introduction to Algorithms', container=container2)
    item5 = Item(name='Post-it Notes', container=container3)
    item6 = Item(name='Pencils', container=container3)

    db.session.add_all([container1, container2, container3])
    db.session.add_all([item1, item2, item3, item4, item5, item6])

    db.session.commit()
