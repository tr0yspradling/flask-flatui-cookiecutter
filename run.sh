# delete debug database
#rm -f dev.db

# activate virtualenv
source env/bin/activate

# set debug flag
export FLASK_DEBUG=TRUE

# upgrade db
#flask db init
#flask db migrate
#flask db upgrade

# launch app
python autoapp.py
