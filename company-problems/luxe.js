// Implement a class that performs async queries but ensures that only N queries are performed in a given time frame (sliding).
// If a new query is requested and the amount of queries exceeds the limit, the query is queued and performed once the time frame allows new queries.
// As an example, we want to only make 3 queries per minute.
// A real life example would be an external API that only allows 3 calls per minute.

class QueriesManager {
    constructor(limit, timeWindow) {
        this.limit = limit;
        this.timeWindow = timeWindow;
        this.startTime = Date.now();
        this.queryCount = 1;
        this.queryQueue = [];
        this.executeQuery = () => {
            return new Promise(resolve => {
                setTimeout(() => {
                    console.log(`API Request executed`);
                    resolve();
                }, 1000);
            });
        }
        this.shouldAdd = true;

    }

    checkTimeInterval() {
        return( Date.now() - this.startTime <= this.timeWindow );
    }

    // query() {
    //     return new Promise(resolve => {
    //         setTimeout(() => {
    //             console.log(`API Request executed`);
    //             resolve();
    //         }, 1000);
    //     });
    // }

    executeQuery() {
        return new Promise(resolve => {
            setTimeout(() => {
                console.log(`API Request executed`);
                resolve();
            }, 1000);
        });
    }

    query() {
        if (this.checkTimeInterval() && this.queryCount <= this.limit) {
            console.log(`queryCount: ${this.queryCount}`);
            this.shouldAdd = true;
            if (this.queryQueue.length == 0) {
                this.queryQueue.push(this.executeQuery);
            }
            var newQuery = this.queryQueue.shift();
            this.queryCount += 1;
            return this.executeQuery();
        }else if (this.checkTimeInterval() == false) {
            this.startTime = Date.now();
            this.queryCount = 1;
            this.queryQueue.push(this.executeQuery);
            return this.query();
        }else if (this.queryCount > this.limit && this.checkTimeInterval()) {
            if (this.shouldAdd) {
                this.shouldAdd = false;
                this.queryQueue.push(this.executeQuery);
                return this.query();
            }else {
                return this.query();
            }

        }
    }

    // query() {
    //     if (this.checkTimeInterval()) {
    //         if (this.queryCount <= this.limit) {
    //             console.log(`queryCount: ${this.queryCount}`);
    //             this.queryCount += 1;
    //             return this.executeQuery();
    //         }else{
    //             console.log(`query count is greater than limit`);
    //             this.queryQueue.push(this.executeQuery);
    //             console.log(this.queryQueue.length);
    //         }
    //     }else{
    //         console.log(`time exceeded`);
    //         console.log(`query count else is: ${this.queryCount}`)
    //         var newQuery = this.queryQueue.shift();
    //         if (newQuery !== undefined || this.queryCount == this.limit + 1) {
    //             this.startTime = Date.now();
    //             this.queryCount = 1;
    //             return this.query();
    //         }
    //     }
    // }
}

const manager = new QueriesManager(3, 4000);

(async function() {
  await manager.query();
  await manager.query();
  await manager.query();

  // 4th
  await manager.query();
  // await manager.query();
  // await manager.query();
})();






// class QueriesManager {
//   constructor(limit, timeWindow) {
//       this._limit = limit;
//       this._timeWindow = timeWindow;
//       this.now = Date.now();
//       this.queue = [];
//       this.current_count = limit;
//       this.firstQueryTime = null;
//   }
//   query() {
//       if (this.current_count > 0){
//           if (this.current_count == limit) {
//               this.firstQueryTime = Date.now()
//           }
//           this.current_count -= 1; // decrement
//           _makeQuery(); // call make query
//       }else{
//           this.queue.push(_makeQuery);
//           setTimeout(this.queue.shift(), this._timeWindow - (Date.now() - this.firstQueryTime));
//       }
//   }
//
//   _makeQuery() {
//       return new Promise(resolve => {
//           setTimeout(resolve, 100);
//       });
//   }
//
//   // async query() {
//   //
//   // }
//   //
//   // // For this example, we just wait for a few ms
//   // async _makeQuery() {
//       // return new Promise(resolve => {
//       //     setTimeout(resolve, 100);
//       // });
//   // }
// }
//
// const manager = new QueriesManager(3, 3600);
//
// (async function() {
//   await manager.query();
//   await manager.query();
//   await manager.query();
//
//   // 4th
//   await manager.query();
//   await manager.query();
//   await manager.query();
// })();



// (function() {})();
//
// function a() {}
