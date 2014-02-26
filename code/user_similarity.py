from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches,
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    # 3) list all user pairs that have jaccard similarity >= 0.5
    ##/

    def extract_businesses(self, _, record):
        """Take in a record. Yield <user_id, business_id>"""
        user_id=record['user_id']
        business_id=record['business_id']
        if record['type'] == 'review':
            #print("user_id: ",user_id,"business_id: ", business_id)
            yield [user_id, business_id]

    def reducer1(self, user_id, business_ids):
        user_business = list(set(business_ids))
        #print("user: ",user_id," businesses: ",user_business)
        yield['a',[user_id, user_business]]


    def user_pairs(self, user_id, user_business):
        '''reducer2
            creates every pair of user/business lists
            ex: [[user1, [bus1, bus3, bus5]], [user2, [bus3, bus4, bus5]]]
        '''
        user_business = list(user_business)
        #print user_business
        for i in user_business:
            next_index = user_business.index(i) + 1
            while next_index < len(user_business):
                j = user_business[next_index]
                #print "user  ",user_business.index(i),"(i) : ",i," user",next_index,"(j): ", j
                yield [i,j]
                next_index += 1
    
    def jaccard(self, i, j):
        '''mapper'''
        #print "i ", i[1], "j ", j[1]
        intersection = len(set(i[1]).intersection(set(j[1])))
        union = len(set(i[1]).union(set(j[1])))
        jaccard = float(intersection / union)
        if jaccard >= 0.5:
            yield [i[0], [j[0], jaccard]]       


    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [
            self.mr(self.extract_businesses, self.reducer1)
            ,self.mr(reducer=self.user_pairs)
            ,self.mr(mapper=self.jaccard)
        ]


if __name__ == '__main__':
    UserSimilarity.run()
