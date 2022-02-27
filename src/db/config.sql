CREATE TABLE flags (
    k TEXT PRIMARY KEY, 
    v INTEGER
);

CREATE TABLE manifest (
    anchor TEXT PRIMARY KEY,
    mtime INTEGER,
    chksum TEXT
);

INSERT INTO flags
VALUES
    ("ZIP", 1),
    ("BUCKET_OK", 0),
    ("INIT", 1);