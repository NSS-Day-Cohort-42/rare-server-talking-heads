CREATE TABLE `User` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `user_name` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    `first_name` TEXT NOT NULL,
    `last_name` TEXT NOT NULL,
    `bio` TEXT NOT NULL
);

CREATE TABLE `Category` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL
);

CREATE TABLE `Tag` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL
);

CREATE TABLE `Post` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `title` TEXT NOT NULL,
    `content` TEXT NOT NULL,
    `pubdate` DATE,
    `header_img` TEXT,
    `user_id` INTEGER NOT NULL,
    `category_id` INTEGER,
    FOREIGN KEY(`user_id`) REFERENCES `User`(`id`),
    FOREIGN KEY(`category_id`) REFERENCES `Category`(`id`)
);

CREATE TABLE `TagPost` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `tag_id` INTEGER NOT NULL,
    `post_id` INTEGER NOT NULL,
    FOREIGN KEY(`tag_id`) REFERENCES `Tag`(`id`),
    FOREIGN KEY(`post_id`) REFERENCES `Post`(`id`)
);

CREATE TABLE `Comment` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `subject` TEXT NOT NULL,
    `content` TEXT NOT NULL,
    `user_id` INTEGER NOT NULL,
    `post_id` INTEGER NOT NULL,
    FOREIGN KEY(`user_id`) REFERENCES `User`(`id`),
    FOREIGN KEY(`post_id`) REFERENCES `Post`(`id`)
);

insert into `User` values (1, 'tbarette0', 'tbarette0@hugedomains.com', 'eUqsHs9bPdtf', 'Thomasina', 'Barette', 'bio');
insert into `User`  values (2, 'tebenezer1', 'tebenezer1@twitter.com', 'F852pgF9ze9', 'Town', 'Ebenezer', 'bio');
insert into`User` values (3, 'cdelchecolo2', 'cdelchecolo2@youku.com', 'HQdyTmfePh', 'Constantia', 'Del Checolo', 'bio');
insert into `User` values (4, 'bburnage3', 'bburnage3@reuters.com', 'M30RJ9Oq', 'Byron', 'Burnage', 'bio');
insert into `User` values (5, 'ohullins4', 'ohullins4@nymag.com', 'xZwWKlA1nb4m', 'Octavia', 'Hullins', 'bio');
insert into `User` values (6, 'jchaytor5', 'jchaytor5@dagondesign.com', 'urwjh8CDLuj', 'Jarad', 'Chaytor', 'bio');
insert into `User`  values (7, 'mmanes6', 'mmanes6@timesonline.co.uk', 'KoOhxCv3iU9', 'Morley', 'Manes', 'bio');
insert into `User`  values (8, 'dphelan7', 'dphelan7@netvibes.com', '750nSjm2Z6E', 'Dorthy', 'Phelan', 'bio');
insert into `User` values (9, 'klumox8', 'klumox8@yellowbook.com', '8VzOOu', 'Kayla', 'Lumox', 'bio');
insert into `User` values (10, 'chaselup9', 'chaselup9@imageshack.us', 'hK6DjKmCFwK1', 'Caryl', 'Haselup', 'bio');

INSERT INTO `Category` values (null, "Category 1");
INSERT INTO `Category` values (null, "Category 2");
INSERT INTO `Category` values (null, "Category 3");
INSERT INTO `Category` values (null, "Category 4");
INSERT INTO `Category` values (null, "Category 5");

INSERT INTO `Tag` values (null, "Tag 1");
INSERT INTO `Tag` values (null, "Tag 2");
INSERT INTO `Tag` values (null, "Tag 3");
INSERT INTO `Tag` values (null, "Tag 4");
INSERT INTO `Tag` values (null, "Tag 5");

insert into `Post`  values (1, 'cblunsden0', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum varius viverra nibh. Praesent semper eleifend nisi, a commodo dolor hendrerit vel. Nam viverra hendrerit lacus, id ullamcorper velit finibus quis. Etiam a ante enim. Aliquam egestas molestie mi cursus commodo. Aenean quis rutrum nibh. Mauris venenatis laoreet tortor, id porta dui iaculis non. Vestibulum leo nunc, auctor quis quam ut, laoreet varius quam. Pellentesque eget nisl suscipit, viverra dolor ac, consectetur leo. Phasellus sagittis diam nec sapien rhoncus ornare. Duis at ante mollis, porttitor nibh at, elementum sapien. Curabitur laoreet, tortor at pharetra aliquam, enim augue pulvinar purus, et tincidunt quam ex et arcu.', '2020-1-1', null, 1, 1);
insert into `Post`  values (2, 'imcquode1', 'Donec scelerisque urna est, vitae vulputate risus mollis quis. Maecenas ullamcorper ut mi non pellentesque. Fusce at mollis nisl, at gravida nunc. Maecenas ut fermentum lectus. Etiam finibus placerat sapien sed dignissim. Donec purus nunc, mattis in ipsum et, hendrerit dictum diam. Nunc iaculis posuere efficitur. Aliquam nec venenatis metus. Mauris dignissim elementum justo ac suscipit. Mauris dignissim, tortor tristique consectetur pellentesque, ante ipsum volutpat justo, quis vulputate ante felis id turpis. Nullam laoreet, tortor et ullamcorper congue, odio elit vestibulum orci, et efficitur velit sem at est. Nullam eget magna a tortor efficitur tempor. In hendrerit, felis cursus efficitur viverra, lorem lectus convallis dui, sagittis suscipit nisl est sit amet odio. Duis a efficitur urna. Cras metus lacus, pretium vel eleifend quis, congue at nisl. Vestibulum in vestibulum enim.','2020-2-1', null, 2, 2);
insert into `Post` values (3, 'bquare2', 'Praesent dapibus odio eget risus ultrices viverra. Aliquam erat volutpat. Pellentesque quis libero pretium, finibus metus quis, volutpat velit. Nam nunc arcu, tempus sit amet vestibulum vitae, placerat sit amet ligula. Praesent nunc odio, aliquam ac iaculis vitae, rutrum a elit. Nam quam enim, egestas vitae bibendum non, lobortis in nisi. Praesent ac euismod turpis. Sed suscipit neque ex, vel fermentum ante condimentum nec. Pellentesque sodales luctus dapibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Quisque sem turpis, rhoncus vitae feugiat ut, laoreet ac lectus. Curabitur quam felis, vestibulum eu tortor eu, finibus feugiat magna. Nulla enim metus, ultrices lobortis tempor molestie, facilisis eu lacus.', '2020-3-1', null, 3, 3);
insert into `Post`  values (4, 'tlauridsen3', 'Suspendisse magna ligula, laoreet sed tristique et, varius nec velit. Praesent nisi diam, imperdiet ut eleifend sed, porttitor eu eros. Mauris gravida, massa sed sollicitudin aliquet, augue libero porta urna, vel convallis arcu ligula ac nibh. Suspendisse odio lectus, efficitur sit amet auctor nec, dignissim non eros. Suspendisse ultrices eros ac porta accumsan. In id tempor eros. Donec vel orci sed ligula rhoncus tristique. Nam eu accumsan augue. Nullam sollicitudin odio nec luctus dignissim. Ut sed velit sed dolor aliquam placerat vel eu turpis. Phasellus pretium tellus in est tempus, eget vestibulum ligula luctus. Donec sed arcu non justo tempus semper. Nulla ut urna neque.', '2020-4-1', null, 4, 4);
insert into `Post` values (5, 'dsloper4', 'Pellentesque purus tellus, dignissim vitae iaculis a, elementum ut erat. Curabitur lobortis egestas nibh ac mattis. Vestibulum porta sed magna nec elementum. Aenean bibendum iaculis lacus. Phasellus suscipit, nibh ac pretium porta, eros mi tincidunt diam, vel molestie metus justo in sem. Cras fermentum enim convallis sollicitudin vestibulum. Praesent non tempus ex.', '2020-5-1', null, 5, 5);

INSERT INTO `TagPost` values (null, 1,3);
INSERT INTO `TagPost` values (null, 2,1 );
INSERT INTO `TagPost` values (null, 3, 1);
INSERT INTO `TagPost` values (null, 1,2);
INSERT INTO `TagPost` values (null, 5,1);

INSERT INTO 'Comment' VALUES (null, 'This is my Subject 1', 'This is my comment 1', 1, 1);
INSERT INTO 'Comment' VALUES (null, 'This is my Subject 2', 'This is my comment 2', 2, 1);
INSERT INTO 'Comment' VALUES (null, 'This is my Subject 3', 'This is my comment 3', 3, 2);
INSERT INTO 'Comment' VALUES (null, 'This is my Subject 4', 'This is my comment 4', 4, 2);
INSERT INTO 'Comment' VALUES (null, 'This is my Subject 5', 'This is my comment 5', 5, 4);


SELECT * FROM Category;
SELECT * FROM Tag;
SELECT * FROM Post;
SELECT * FROM TagPost;
SELECT * FROM Comment;
SELECT * FROM User;


SELECT  
    p.id,
    p.title,
    p.content,
    t.name
    
FROM Post p
JOIN TagPost tp on tp.post_id = p.id
JOIN Tag t on t.id = tp.tag_id
WHERE p.id = 2;

SELECT 
    p.title,
    c.subject,
    c.content,
    u.user_name
FROM Post p 
JOIN Comment c ON c.post_id = p.id 
JOIN User u ON u.id = c.user_id
WHERE p.id = 2;