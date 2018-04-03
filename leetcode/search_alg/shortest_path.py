var I = 1;
while( I < 4 ) {
    db.get('.....', function(err, result) {
        console.log("Result", I);
    }
  I++;
}
