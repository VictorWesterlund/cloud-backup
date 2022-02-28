CREATE TABLE flags (
    k TEXT PRIMARY KEY, 
    v INTEGER
);

CREATE TABLE manifest (
    anchor TEXT PRIMARY KEY,
    chksum INTEGER
);

INSERT INTO flags
VALUES
    ("ZIP", 1),
    ("BUCKET_OK", 0),
    ("INIT", 1);