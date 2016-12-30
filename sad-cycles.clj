(ns myfirstclojureproject.core)
(require '[clojure.string :as str])


(defn expt [pow x] (apply * (repeat pow x)))

(def base 2)
(def mynumber "13")

(defn str->numbers 
  [instr] 
  (str/split instr #""))
  
(defn make-numbers 
  [vecstrnum]
  (map (fn [x] (Integer. x)) vecstrnum) )

(defn sumup 
  [vecnum]
  ( reduce + (map (fn [x] (expt base x)) (make-numbers vecnum))))

(defn comp-vec
  "Compares each element of the vectors to be equal"
  [v1 v2]
  (if (< (count v1) (count v2))
    false
    (if (empty? v2)
      true
      (if (= (first v1) (first v2))
      (comp-vec (rest v1) (rest v2))
        false
        ))))


(defn vec-vec
  "Find a vector in a vector"
  [src subvec]
  (let [rest-vec (drop-while #(not(= % (first subvec))) src)]
  (if (> (count rest-vec) 0 )
    (if (comp-vec rest-vec subvec)
      subvec
      (vec-vec (rest rest-vec) subvec)
    )
  )))

(defn islast-eq
  "Checks if the last elements are a sub sequence"
  [srcvec n]
  (let [len (count srcvec)
        va (drop (- len n) srcvec)
        vb (take n (drop (- len (* n 2)) srcvec))]
    (if (<= (- len n) 0)
      ()
      (let [result (vec-vec va vb)]
        (if (empty? result)
          (if (>= n (/ len 2))
            ( )
            (islast-eq srcvec (inc n))
          )
          result
          )
        )
      )
    )
  )


(defn sad-cycle
  "Sad cylce challenge #215 Easy from 2015-05-18"
  []
  (loop [strnumber mynumber, accu ()]
    (let [summe (sumup (make-numbers (str->numbers strnumber)))
          total (flatten (list accu summe))
          result (islast-eq total 1)]
      (if (empty? result)
        (recur (str summe) total)
        (println "Done " result))))
  )

