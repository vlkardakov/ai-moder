from database_super import connect_database

if __name__ == '__main__':
    connection = connect_database()
    cursor = connection.cursor()
    try:
        for i in range(10000):
            for x in range(100):
                cursor.execute("""INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!'); 
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');
    INSERT INTO examples (text) VALUES ('МЯУ!!!');""")
            print(i*50000)
        # while True:
        #     query = ''
        #     print(r'Введите запрос:')
        #     text = input()
        #     while text != '':
        #         query += f'\n{text}'
        #         text = input()
        #
        #
        #     # print(f'Вы ввели запрос: \n{query}')
        #     try:
        #         cursor.execute(query)
        #     except Exception as e:
        #         print(f'Ошибка при выполнении запроса: {e}')
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
    except KeyboardInterrupt:
        connection.commit()# сохранение
        cursor.close()
        connection.close()
        print("BYE!")