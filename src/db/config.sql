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
    ("COMPRESS", 1),
    ("BUCKET_OK", 0),
    ("INIT", 1);